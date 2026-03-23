"""
TP6
Par Camille Voisin 404
Commencé le 13 février 2026
finit le :
"""

import arcade
import random as rd

from game_state import GameState
from Attacks import AttackType, AttackAnimation

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Starting Template"


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """


    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.BLACK
        self.player_sprite = None
        self.computer_sprite = None
        self.players_list = None
        self.player_point = 0
        self.computer_point = 0
        self.game_state = GameState.NOT_STARTED
        self.player_attack_choosen = False
        self.computer_attack_type = 0

        self.reset()

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        self.player_sprite = arcade.Sprite("assets/faceBeard.png", 0.35)
        self.player_sprite.position = (305, 350)
        self.computer_sprite = arcade.Sprite("assets/compy.png", 1.70)
        self.computer_sprite.position = (1000, 350)
        self.attack_type = AttackType


        self.rock_sprite = AttackAnimation(AttackType.ROCK)
        self.paper_sprite = AttackAnimation(AttackType.PAPER)
        self.scissors_sprite = AttackAnimation(AttackType.SCISSORS)
        self.random_sprite = AttackAnimation(AttackType.nothing)
        self.rock_sprite.position = (145, 198)
        self.paper_sprite.position = (320, 200)
        self.scissors_sprite.position = (462, 200)
        self.random_sprite.position = (1000, 195)
        self.players_list = arcade.SpriteList()
        self.players_list.append(self.player_sprite)
        self.players_list.append(self.computer_sprite)
        self.hands_list = arcade.SpriteList()
        self.player_attack_type = AttackType.nothing
        self.computer_attack_type = AttackType.nothing
        self.hands_list.append(self.rock_sprite)
        self.hands_list.append(self.paper_sprite)
        self.hands_list.append(self.scissors_sprite)
        self.hands_list.append(self.random_sprite)
        self.player_point = 0
        self.computer_point = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        self.players_list.draw()
        self.hands_list.draw()
        arcade.draw_text("Roche, Papier, Ciseaux", 250, 650, arcade.color.BLACK_BEAN, 70)
        if self.game_state == GameState.ROUND_DONE or self.game_state == GameState.NOT_STARTED:
            arcade.draw_text("Appuyez sur espace pour commencer!", 200, 550, arcade.color.CYAN, 50)
        elif self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text("Appuyez sur une image pour faire une", 185, 550, arcade.color.CYAN, 50)
            arcade.draw_text("attaque!", 600, 500, arcade.color.CYAN, 50)
        arcade.draw_text("Votre attaque est :", 200, 450, arcade.color.GRAY, 50)
        arcade.draw_text(self.player_attack_type, 700, 450, arcade.color.BLUE_VIOLET, 50)
        left = 70
        right = 220
        for i in range(3):
            arcade.draw_lrbt_rectangle_outline(left, right,
                                               120, 270, arcade.color.DARK_SALMON, 3)
            left += 160
            right += 160
        arcade.draw_lrbt_rectangle_outline(926, 1076,
                                           120, 270, arcade.color.DARK_SALMON, 3)
        arcade.draw_text("Le Pointage du joueur est :", 70, 90, arcade.color.CYAN, 30)
        arcade.draw_text("Le Pointage de l'ordinateur est :", 800, 90, arcade.color.CYAN, 20)
        arcade.draw_text(self.player_point, 510, 90, arcade.color.CYAN, 30)
        arcade.draw_text(self.computer_point, 1140, 90, arcade.color.CYAN, 20)
        if self.game_state == GameState.NOT_STARTED:
            pass
        # les attaques du joueur
        # retour au sprite de base


        if self.player_point == 3:
            arcade.draw_text("VICTOIRE DU JOUEUR", 400, 400, arcade.color.GREEN, 45)
            self.game_state = GameState.GAME_OVER
        elif self.computer_point == 3:
            arcade.draw_text("VICTOIRE DE L'ORDI", 400, 400, arcade.color.RED, 45)
            self.game_state = GameState.GAME_OVER
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        self.rock_sprite.on_update(delta_time)
        self.paper_sprite.on_update(delta_time)
        self.scissors_sprite.on_update(delta_time)
        if self.game_state != GameState.ROUND_ACTIVE:
            return
        if self.game_state == GameState.ROUND_ACTIVE and self.player_attack_choosen:
            ComputerAttack = rd.randint(0, 2)
            if ComputerAttack == 0:
                self.computer_attack_type = AttackType.ROCK
                print(self.computer_attack_type)
            elif ComputerAttack == 1:
                self.computer_attack_type = AttackType.PAPER
                print(self.computer_attack_type)
            elif ComputerAttack == 2:
                self.computer_attack_type = AttackType.SCISSORS
                print(self.computer_attack_type)
            if self.player_attack_type == self.computer_attack_type:
                print("Égalité")
                self.game_state = GameState.ROUND_DONE
            elif self.player_attack_type == AttackType.ROCK:
                self.rock_sprite = arcade.Sprite("assets/srock-attack.png")
                if self.computer_attack_type == AttackType.PAPER:
                    self.computer_point += 1
                    print(self.computer_point)
                    print("CV")
                    self.game_state = GameState.ROUND_DONE
            elif self.player_attack_type == AttackType.PAPER:
                if self.computer_attack_type == AttackType.SCISSORS:
                    self.computer_point += 1
                    print(self.computer_point)
                    print("CV")
                    self.game_state = GameState.ROUND_DONE
            elif self.player_attack_type == AttackType.SCISSORS:
                if self.computer_attack_type == AttackType.ROCK:
                    self.computer_point += 1
                    print(self.computer_point)
                    print("CV")
                    self.game_state = GameState.ROUND_DONE
            if self.player_attack_type == AttackType.PAPER:
                if self.computer_attack_type == AttackType.ROCK:
                    self.player_point += 1
                    print(self.player_point)
                    print("PV")
                    self.game_state = GameState.ROUND_DONE
            if self.player_attack_type == AttackType.SCISSORS:
                if self.computer_attack_type == AttackType.PAPER:
                    self.player_point += 1
                    print(self.player_point)
                    print("PV")
                    self.game_state = GameState.ROUND_DONE
            if self.player_attack_type == AttackType.ROCK:
                if self.computer_attack_type == AttackType.SCISSORS:
                    self.player_point += 1
                    print(self.player_point)
                    print("PV")
                    self.game_state = GameState.ROUND_DONE
            elif self.player_point >= 3:
                self.game_state = GameState.GAME_OVER
                print("VICTOIRE JOUEUR")
            elif self.computer_point >= 3:
                self.game_state = GameState.GAME_OVER
                print("VICTOIRE ORDI")
        else:
            return

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        state = 0
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE
                print("ACTIVE")
            elif self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE
                self.player_attack_choosen = False

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if self.game_state != GameState.ROUND_ACTIVE:
            return
        elif self.game_state == GameState.ROUND_ACTIVE:
            if self.rock_sprite.collides_with_point((x, y)):
                print("Clicked rock!")
                self.player_attack_choosen = True
                self.player_attack_type = AttackType.ROCK


            elif self.paper_sprite.collides_with_point((x, y)):
                print("Clicked paper!")
                self.player_attack_choosen = True
                self.player_attack_type = AttackType.PAPER

            elif self.scissors_sprite.collides_with_point((x, y)):
                print("Clicked scissors!")
                self.player_attack_choosen = True
                self.player_attack_type = AttackType.SCISSORS

            else:
                return


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
