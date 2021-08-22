from .start_handler import dp
from .back_handler import dp
from .help_handler import dp
from .general_handlers import dp
from .socialnetwork_handlers import dp
from .structure_handlers import dp
from .other_handler import dp, keyboards, commands
from .query_handlers import dp

__all__ = [
    'dp',
    'keyboards',
    'commands'
]