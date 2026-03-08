# 🧩 8 Puzzle Game using Pygame

A simple yet interactive **8 Puzzle Game built using Python and Pygame**.
The game consists of a **3 × 3 sliding puzzle** where numbered tiles must be arranged in the correct order by sliding them into the empty space.

This project demonstrates:

* 🎮 Game development basics with **Pygame**
* 🧠 Problem solving with **grid-based logic**
* 🎨 UI design with **custom colors and tile rendering**
* ⌨️ Keyboard-based movement control

---

# 🎮 Game Preview
"https://github.com/user-attachments/assets/5418fd4a-987e-4881-ba1c-bb31b9e90824" 

```

```

Example:

https://github.com/user-attachments/assets/942b868d-d2e8-46c7-a9c5-0a67a4be137e

---

# 🧠 Game Concept

The **8 Puzzle** is a classic sliding puzzle consisting of:

* **8 numbered tiles**
* **1 empty space**
* A **3×3 grid**

### Objective

Arrange the tiles in **ascending order**:

```
1 2 3
4 5 6
7 8 _
```

Where **_ represents the empty space**.

You move tiles by sliding them into the empty space.

---

# 🎮 Controls

| Key            | Action          |
| -------------- | --------------- |
| ⬆️ Up Arrow    | Move tile up    |
| ⬇️ Down Arrow  | Move tile down  |
| ⬅️ Left Arrow  | Move tile left  |
| ➡️ Right Arrow | Move tile right |

---

# ⚙️ Features

✨ Clean graphical interface
🎨 Rounded tiles with modern color theme
🎲 Random puzzle generation every run
⌨️ Keyboard-based movement controls
🧩 Smooth tile swapping logic

---

# 🏗️ Project Structure

```
8-puzzle-game
│
├── puzzle_game.py
├── README.md
└── assets
     └── output.png
```

---

# 🧪 Technologies Used

* **Python**
* **Pygame**
* **Random module**

---

# 💻 Installation & Setup

### 1️⃣ Install Python

Download Python from
[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### 2️⃣ Install Pygame

Run the following command:

```bash
pip install pygame
```

---

### 3️⃣ Run the Game

```bash
python puzzle_game.py
```

---

# 🧩 How the Game Works

### 1️⃣ Puzzle Generation

The board is created by **randomly shuffling numbers from 0–8**.

```python
nums = list(range(9))
random.shuffle(nums)
```

`0` represents the **empty tile**.

---

### 2️⃣ Finding the Empty Tile

The game searches for the tile containing **0** to determine where movement can occur.

```python
if puzzle[i][j] == 0:
```

---

### 3️⃣ Moving Tiles

Arrow keys trigger movement by swapping the empty tile with an adjacent tile.

Example:

```python
if event.key == pygame.K_UP:
    move(1,0)
```

---

### 4️⃣ Rendering the Board

Each frame draws the grid with:

* Colored tiles
* Numbers
* Rounded borders

```python
pygame.draw.rect(screen, TILE_COLOR, rect, border_radius=15)
```

---

# 🎨 UI Design

Color Theme Used:

| Element    | Color      |
| ---------- | ---------- |
| Background | Dark Blue  |
| Tiles      | Light Blue |
| Text       | White      |
| Empty Tile | Dark Grey  |

This gives the game a **clean modern appearance**.

---

# 🚀 Future Improvements

Possible enhancements:

* 🏆 Win detection
* ⏱️ Timer system
* 🔢 Move counter
* 🔁 Reset / Shuffle button
* 🤖 Auto solver (AI / BFS / A*)

---

# 📚 Learning Outcomes

Through this project you will understand:

* Game loops in Pygame
* Grid-based puzzle logic
* Event handling
* Rendering UI elements
* Python game development basics

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve the game:

1. Fork the repository
2. Create a new branch
3. Make improvements
4. Submit a pull request

---

# ⭐ If you like this project

Give the repository a ⭐ on GitHub!

---

