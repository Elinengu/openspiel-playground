# from ~/open_spiel/python/visualizations/treeviz.py
import pyspiel
from open_spiel.python.visualizations import treeviz

game = pyspiel.load_game("tic_tac_toe")
tree = treeviz.GameTree(game, depth_limit=3)
tree.draw("tic_tac_toe_tree.svg", prog="dot")
