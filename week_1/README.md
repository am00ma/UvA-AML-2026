# Week 1: Introduction to Python

Welcome to the **Applied Machine Learning** course!

- [Week 1: Introduction to Python](#week-1-introduction-to-python)
  - [📚 Overview](#-overview)
    - [Why Python?](#why-python)
  - [🛠️ Setup Instructions](#️-setup-instructions)
    - [Installation](#installation)
    - [Running Python Code](#running-python-code)
    - [Launching Jupyter Notebook](#launching-jupyter-notebook)
    - [⭐️ Recommended Tools](#️-recommended-tools)
  - [❓ Frequently Asked Questions](#-frequently-asked-questions)
  - [📝 Assignment: Week 1](#-assignment-week-1)

## 📚 Overview

During this course, we will use [Python](https://www.python.org) to perform matrix computations, image manipulation, and retrieval tasks. This week provides an introduction to Python and essential libraries you'll need throughout the course.

> **📓 Main Resource:** See [`Intro.ipynb`](Intro.ipynb) for detailed examples and exercises.

### Why Python?

Python is a popular high-level programming language with an emphasis on code readability and concise syntax. Key features that make it easy to learn:

- **Dynamic type system** – No need to explicitly declare variable types (`int`, `float`, `string`). Python infers them automatically.
- **Automatic memory management** – No manual memory allocation or pointer management required.
- **Rich library ecosystem** – From math libraries to game engines, thousands of packages are ready to use.

Feel free to experiment with the language to understand how it works. We're confident that those new to Python will quickly come to appreciate it!

---

## 🛠️ Setup Instructions

### Installation

> **Note for Linux users:** Most distributions come with Python pre-installed, though using `uv` still has advantages for package management.

**Recommended:** Python 3.6 or newer via **`uv`**

[`uv`](https://docs.astral.sh/uv/getting-started/installation/) is a scientific Python distribution that includes:

- Python interpreter
- Virtual environment manager
- Easy installation for popular scientific libraries
- Useful utilities

Note that other ways of setting up Python and packages exist. If you are comfortable using the command line, check out the Recommended Tools section below!

**Installation steps:**

1. Follow the installation instructions
2. Create and activate the environment:

```bash
uv sync
source .venv/bin/activate
```

### Running Python Code

There are several ways to execute Python code:

1. **Script files** – Create a `.py` file and run: `python <filename>`
2. **Interactive interpreter** – Type `python` in the command line to test short snippets
3. **Jupyter Notebook** ⭐ **(Recommended for this course)**

### Launching Jupyter Notebook

Jupyter Notebook combines the Python interpreter, Markdown documentation, and visualization tools in a browser-based interface.

**To launch:**

```bash
jupyter notebook
```

**To open in a specific folder:**

```bash
cd /path/to/directory
jupyter notebook
```

> **Windows users:** If the directory is on a different drive, type the drive letter first (e.g., `D:` then press Enter).

### ⭐️ Recommended Tools

#### 1. Visual Studio Code

Jupyter notebooks can be launched and edited from a regular browser window as above, but most often people use dedicated editors, the most popular ([by far](https://survey.stackoverflow.co/2025/technology#most-popular-technologies-dev-envs)) being Visual Studio Code, freely available [here](https://code.visualstudio.com/).

You can then edit and run Jupyter notebooks in VS Code, just like regular files: https://code.visualstudio.com/docs/datascience/jupyter-notebooks. It is more convenient to use than a browser window, and is better customizable with lots of packages, themes, etc.

#### 2. Git / GitHub

Git is the most popular version control system. You can "commit" your code as you make changes (think like checkpoints) and then can go back to previous versions even if you delete files. It also allows you to have multiple "branches" of your code with different versions, and a lot more. Check the tutorial here to get started: https://rogerdudler.github.io/git-guide/

We highly recommend you use Git to track your changes and push your code to [GitHub](https://github.com/), so that e.g. even if you accidentally delete files you can recover your progress.

#### 3. `uv` Package Manager

`uv` is a popular package manager for Python, which can be faster and more convenient to use than Conda or the default `pip`. Check the installation instructions and the guides [here](https://docs.astral.sh/uv/) to get started.

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>Q: How do I install required packages in a new virtual environment?</strong></summary>

**A:** Use `uv` or `pip` to install packages. For this course, you'll need:

- **numpy** – Numerical computing
- **scipy** – Scientific computing
- **matplotlib** – Plotting and visualization
- **scikit-learn** – Machine learning algorithms
- **requests** – HTTP requests

```bash
source .venv/bin/activate
uv add numpy scipy requests
uv add scikit-learn
uv add matplotlib
```

</details>

<details>
<summary><strong>Q: How can I get the materials from GitHub?</strong></summary>

**A:** Choose one of these methods:

1. **Download ZIP** – Visit the repository and download the `.zip` archive (simplest)
2. **GitHub Desktop** – [Download the client](https://desktop.github.com), visit the repository, and click "Open in Desktop"
3. **Git CLI** – Clone via command line (requires [Git installation](https://git-scm.com/downloads)):
   ```bash
   git clone git@github.com:maxvanspengler/UVA_AML23.git
   ```
   [Git tutorial](https://try.github.io/) for beginners

</details>

---

## 📝 Assignment: Week 1

Complete the exercises in [`Intro.ipynb`](Intro.ipynb). Each function you implement will be tested for correctness using **automark**.

**Enjoy coding!** 🚀
