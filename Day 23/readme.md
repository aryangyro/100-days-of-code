This project is an arcade-style crossing game built using Python’s turtle module, focused on understanding real-time game loops, rendering, and state management. The player navigates across moving obstacles while the game dynamically updates difficulty, score, and visual themes.

Throughout development, the project evolved beyond basic gameplay into solving real game-development problems, such as collision detection accuracy, preventing repeated event triggers, managing object lifecycles without clearing the entire screen, and handling redraws correctly when using tracer(0) and manual screen.update() calls.

A major part of the work involved fixing rendering issues—like text not updating color, objects still appearing after game over, and UI elements reappearing unexpectedly—by learning the difference between state changes vs visual redraws. The game now properly separates gameplay state and game-over state, redraws UI elements only when required, and allows safe theme switching even after the game ends.

Overall, this project strengthened practical understanding of Python OOP, event-based rendering, game state control, and how small ordering mistakes in a game loop can cause subtle but critical bugs. It serves as a solid foundation for building more complex interactive games.
