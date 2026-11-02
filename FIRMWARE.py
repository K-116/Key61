import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# ==========================================
# PIN CONFIGURATION
# Adapt these pins to match your microcontroller and wiring.
# A full-size keyboard typically requires 6 rows and 21+ columns.
# ==========================================
keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6,
    board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13,
    board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20
)
keyboard.row_pins = (
    board.GP21, board.GP22, board.GP23, board.GP24, board.GP25, board.GP26
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ==========================================
# KEYMAP DEFINITION
# Layer 0: Standard ANSI Full Size
# Layer 1: Function Layer (activated by MO(1))
# ==========================================

# Helper for transparent keys (falls through to lower layer)
_______ = KC.TRNS
# Momentary layer 1
MO1 = KC.MO(1)

keyboard.keymap = [
    # Layer 0: Base Layer (ANSI Full Size)
    [
        # Row 1: Function row
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCR, KC.SLCK, KC.PAUS,
        # Row 2: Number row
        KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.INS, KC.HOME, KC.PGUP, KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
        # Row 3: Top alpha row
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL, KC.END, KC.PGDN, KC.P7, KC.P8, KC.P9, KC.PPLS,
        # Row 4: Home row
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.P4, KC.P5, KC.P6,
        # Row 5: Bottom alpha row
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.P1, KC.P2, KC.P3, KC.PENT,
        # Row 6: Modifier row
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, MO1, KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT, KC.P0, KC.PDOT
    ],
    
    # Layer 1: Function Layer (Example: Media & Navigation)
    [
        # Row 1: Function keys become media keys (example)
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        # Row 2
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        # Row 3
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        # Row 4
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        # Row 5
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        # Row 6
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______
    ]
]

if __name__ == '__main__':
    keyboard.go()
