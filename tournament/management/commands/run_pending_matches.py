import random
import logging

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from tournament.models import Challenge
from lightcycle.arena import LightCycleArena
from lightcycle.player import Player

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Run queued matches."

    def handle(self, *args, **options):
        if len(args) > 0:
            raise CommandError('Too many arguments.')

        count = 0
        for count, challenge in enumerate(Challenge.objects.filter(played=False).order_by('creation_date')):
            try:
                logger.info('Running Challenge "%s".' % challenge)
                player1 = Player(challenge.challenger_bot.owner.user, challenge.challenger_bot.code)
                player2 = Player(challenge.challenged_bot.owner.user, challenge.challenged_bot.code)
                players = [player1, player2]
                random.shuffle(players)
                arena = LightCycleArena(players, settings.ARENA_WIDTH, settings.ARENA_HEIGHT)
                result = arena.start()
                print result
                challenge.played = True
                challenge.elapsed_time = result['elapsed_time']
                if 'winner' in result:
                    challenge.winner_bot = [player.bot for player in players if player.name == result['winner']][0]
                # TODO assign scores!

            except Exception as ex:
                msg = 'Error running Challenge "%s" ("%s")' % (challenge, ex)
                logger.error(msg)
                raise CommandError(msg)
        print 'Finished running %d matches.' % count
