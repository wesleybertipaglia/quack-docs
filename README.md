# 🦆 Quack Docs

**Quack Docs** is your AI-powered documentation sidekick, built on **Amazon Q** to help you write, clean, and maintain beautiful code documentation—without the grunt work.

Whether you're managing a solo project or collaborating across teams, Quack Docs automates documentation with precision and ease.

## 📌 Table of Contents

* [🚀 What It Does](#-what-it-does)
* [✨ Key Features](#-key-features)
* [🛠️ How It Works](#️-how-it-works)
* [📦 Getting Started](#-getting-started)
* [🧪 Usage](#-usage)
* [🤝 Contribute](#-contribute)
* [📄 License](#-license)

## 🚀 What It Does

Quack Docs streamlines code documentation by:

* 📄 **Generating clean, structured Markdown** documentation from your codebase.
* 🧠 **Injecting smart, context-aware docstrings** directly into your code—without altering logic.
* ⚡ **Boosting code clarity and maintainability**, saving you time for what matters: building.

## ✨ Key Features

* 🔍 **Auto language detection** via file extensions (supports Python, JS, Go, Java, C++, and more).
* 📑 **Markdown export** with elegant formatting and syntax-highlighted code blocks.
* 🧾 **Inline docstring injection** powered by Amazon Q’s understanding—safe and non-destructive.
* 💬 **CLI-first workflow**, easy to integrate into any dev pipeline.

## 🛠️ How It Works

Under the hood, Quack Docs leverages the **Amazon Q CLI** to analyze and document your source files.

Choose between two modes:

* **Markdown mode**: Generates external `.md` docs.
* **In-place mode**: Enhances code with inline docstrings.

## 📦 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/wesleybertipaglia/quack-docs.git
cd quack-docs
```

### 2. Install Dependencies

```bash
make install
```

### 3. Set up Amazon Q CLI

Follow [these steps](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html) to install and authenticate:

```bash
q login
```

## 🧪 Usage

### Generate Markdown Documentation

```bash
python main.py --file path/to/your_file.py
```

➡️ Creates a Markdown file like:
`./docs/quack_your_file_20250510_103000.md`

You can also choose a custom output directory:

```bash
python main.py --file path/to/your_file.py --output ./my_docs/
```

➡️ Creates:
`./my_docs/quack_your_file_20250510_103000.md`

### Insert Docstrings into Your Code

```bash
python main.py --file path/to/your_file.py --inplace
```

➡️ Overwrites your file with inline docstrings.

You can optionally save the modified file into a different directory while preserving its filename:

```bash
python main.py --file path/to/your_file.py --inplace --output ./src/
```

➡️ Saves:
`./src/your_file.py`

⚠️ **Important:** The `--output` parameter must always be a **directory path**, not a full file path.

### 📌 Quick Reference

| Mode     | Description                            | Default Output         | Customizable     |
| :------- | :------------------------------------- | :--------------------- | :--------------- |
| Markdown | Generates external `.md` documentation | `./docs/`              | ✅ via `--output` |
| In-place | Inserts docstrings into your code file | Overwrites source file | ✅ via `--output` |


## 🤝 Contribute

Suggestions, issues, or ideas? Open a PR or file an issue—we’d love to hear from you!

## 📄 License

MIT License. See the [LICENSE](LICENSE) file for details.
