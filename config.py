import torch

from petals.constants import PUBLIC_INITIAL_PEERS


INITIAL_PEERS = ['/ip4/54.164.52.79/tcp/8989/p2p/QmR7G6GZzeQeJoXfTovp8PJdJ7qxKYFwXUa2fp9p6BYdDi']

MODEL_NAMES = ["bigscience/bloom-petals", "bigscience/bloomz-petals", "bigscience/bloom-7b1-petals"]
DEFAULT_MODEL_NAME = "bigscience/bloomz-petals"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TORCH_DTYPE = torch.bfloat16

STEP_TIMEOUT = 5 * 60
MAX_SESSIONS = 50  # Has effect only for API v1 (HTTP-based)
