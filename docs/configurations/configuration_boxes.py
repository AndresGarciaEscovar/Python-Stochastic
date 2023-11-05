"""
  Constains the configuration parameters for the box. ALL LENGHT VALUES ARE IN
  CENTIMETERS.
"""


# ##############################################################################
# Units
# ##############################################################################

# Units.
UNITS = "cm"

# ##############################################################################
# Constants
# ##############################################################################

# ------------------------------------------------------------------------------
# Box
# ------------------------------------------------------------------------------

# Spacing between images.
PAGE_WIDTH: float = 15
SPACING: float = 0.25

# Actual box width and height: Square.
BOX_WIDTH: float = (PAGE_WIDTH - 2 * SPACING) / 3
BOX_HEIGHT: float = BOX_WIDTH
BOX_MARGIN: float = (BOX_WIDTH + BOX_HEIGHT) * 0.5 * 0.065

# Standard box position.
BOX_POSITION_TOP: tuple = (0, 0)
BOX_POSITION_BOTTOM: tuple = (BOX_WIDTH, -BOX_HEIGHT)

# Other standard positions.
LABEL_POSITION_MAIN: tuple = (
    BOX_POSITION_BOTTOM[0] * 0.5, BOX_POSITION_BOTTOM[1] + BOX_MARGIN
)

LATTICE_POSITION_TICKS: tuple = (
    BOX_POSITION_TOP[0] + BOX_MARGIN, BOX_POSITION_BOTTOM[1] * 3 / 7
)

TITLE_BOX_POSITION_TOP: tuple = (0, 0)
TITLE_BOX_POSITION_BOTTOM: tuple = tuple(x * 0.15 for x in BOX_POSITION_BOTTOM)

# Standard lengths.
LENGTH_LATTICE: float = BOX_WIDTH - 2 * BOX_MARGIN


# ------------------------------------------------------------------------------
# Elements
# ------------------------------------------------------------------------------


# Arrow and lines dimensions; 1/4 of the box height.
FACTOR = 1 / 11
ARROW_LENGTH = BOX_WIDTH * FACTOR
ARROW_HEIGHT = BOX_HEIGHT * FACTOR

TICK_HEIGHT = ARROW_HEIGHT
TICK_LENGTH = ARROW_LENGTH

CIRCLE_RADIUS = (BOX_WIDTH + BOX_HEIGHT) * 0.015
SEPARATION_HORIZONTAL = BOX_WIDTH * 0.03
SEPARATION_VERTICAL = BOX_HEIGHT * 0.01


# ------------------------------------------------------------------------------
# Boxes Specifications.
# ------------------------------------------------------------------------------


# Number of rows and columns in the grid.
ROWS = 4
COLS = 3

# Grid with the offset for each box.
WLOC = BOX_WIDTH + SPACING
HLOC = BOX_HEIGHT + SPACING
OFFSETS = tuple(
    tuple((j * HLOC, i * WLOC) for j in range(COLS)) for i in range(ROWS)
)
