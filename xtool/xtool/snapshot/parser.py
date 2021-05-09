import logging

from parser import Parser


class SnapshotParser(Parser):
    """
    Parser for snapshot-related actions.
    """

    logger = logging.getLogger('SnapshotParser')

    """
    See Parsers#addActions()
    """
    @staticmethod
    def addActions(subParsers, topLevel=False):
        if not topLevel:
            createParser = subParsers.add_parser('create', aliases=['c'], help='create a new snapshot')
            createParser.add_argument(
                'instance_name',
                help='the name of the instance to snapshot'
            )

            restoreParser = subParsers.add_parser('restore', aliases=['r'], help='restore an existing snapshot')
            restoreParser.add_argument(
                'instance_name',
                help='the name of the snapshot to restore'
            )
            restoreParser.add_argument('-o', '--overwrite', action='store_true',
                                       help='overwrite an existing instance if needed')

    """
    See Parsers#handleArgs()
    """
    def handleArgs(self, args, action):
        if action in ['create', 'c']:
            self.snapshotManager.create(args.entity_name)
        elif action in ['restore', 'r']:
            self.snapshotManager.restore(args.entity_name, args.overwrite)
