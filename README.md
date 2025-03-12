# Asteroids-Pygame

A classic Asteroids game built using Pygame. This project replicates the mechanics of the iconic arcade game, featuring player movement, shooting, asteroid collisions, and splitting.

## Features

- **Player Controls**: Rotate and move the spaceship using keyboard controls (WASD keys).
- **Shooting Mechanics**: Shoot projectiles to destroy asteroids.
- **Asteroid Collision**: Asteroids break into smaller pieces when hit by projectiles.
- **Game Over Logic**: The game ends when the player collides with an asteroid.
- **Visual Effects**: Asteroids and bullets are rendered dynamically using Pygame's drawing methods.

## Gameplay

- **Move the spaceship**: Use the W, A, S, and D keys to move and rotate the player spaceship.
- **Shoot bullets**: Press the spacebar to shoot a bullet at approaching asteroids.
- **Asteroids**: Asteroids split into smaller ones when hit by bullets and disappear when destroyed.
- **Game Over**: Colliding with an asteroid results in game over.

# Installation Instructions

## 1. Ensure Python3, Pip3, and Git are installed:

### For Windows:
#### Python:
- Download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
- During installation, make sure to check the box that says "Add Python to PATH".
- Verify installation by running in **Command Prompt**:
    ```bash
    python3 --version
    pip3 --version
    ```

#### git:
- Download and install Git from [https://git-scm.com/download/win](https://git-scm.com/download/win).
- Verify installation by running in **Command Prompt**:
    ```bash
    git --version
    ```

### For macOS:
#### Python 3 (and pip) are usually pre-installed. To check:
```bash
python3 --version
pip3 --version

- If missing, install Python 3 using:
    ```bash
    brew install python3
    ```

#### git:
- Git is generally pre-installed, but you can check with:
    ```bash
    git --version
    ```
- If not installed, use:
    ```bash
    brew install git
    ```

### For Linux (Ubuntu/Debian):
#### Python 3 and pip:
- Check if installed:
    ```bash
    python3 --version
    pip3 --version
    ```
- If not installed, run:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

#### git:
- Check if installed:
    ```bash
    git --version
    ```
- If not installed, run:
    ```bash
    sudo apt install git
    ```

---

## 2. Clone the repository to your local machine:
Before cloning the repository, make sure **git** is installed. To clone the repository, run the following command in **Command Prompt** (Windows) or **Terminal** (macOS/Linux):

```bash
git clone https://github.com/wesonga/Asteroids-Pygame.git
```

---

## 3. Navigate to the project directory:
Once the repository is cloned, change into the project directory:

```bash
cd Asteroids-Pygame
```

---

## 4. Set up a virtual environment (recommended to avoid dependency conflicts):
### For Windows:
Create a virtual environment using:

```bash
python -m venv venv
```

### For macOS/Linux
Create a virtual environment using:

```bash
python3 -m venv venv
```

---

## 5. Activate the virtual environment:
### For Windows:
Activate the virtual environment with:
```bash
venv\Scripts\activate
```

### For macOS/Linux
Activate the virtual environment with:
```bash
source venv/bin/activate
```

---

## 6. Install the required dependencies:
Once the virtual environment is activated, install pygame by running:
```bash
pip install pygame
```

---

## 7. Run the game
After the dependencies are installed, run the game with:
```bash
python3 main.py
```

---

## License
This project is open-source and available under the **[MIT License](LICENSE)**.
