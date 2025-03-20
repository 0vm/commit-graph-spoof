# Contribution Graph Date Spoofer

This script automatically creates a GitHub repository, makes a fake commit from 1970, and pushes it.
![{475DA972-F465-4E05-948D-D7EC12C9E030}](https://github.com/user-attachments/assets/c8a6a54b-f0f9-48ee-a9e4-d8cd3101522e)

## Prerequisites

- **Git** must be installed on your system.
  - **Windows**: [Download Git](https://git-scm.com/download/win)
  - **MacOS**: Install via Homebrew:
    ```bash
    brew install git
    ```
  - **Linux**: Install via package manager:
    ```bash
    sudo apt install git -y  # Debian/Ubuntu
    sudo dnf install git -y  # Fedora
    ```

- **Python 3** must be installed.
  - Check by running:
    ```bash
    python --version
    ```

## Usage

1. **Get a GitHub Personal Access Token (PAT)**
   - Go to [GitHub Tokens](https://github.com/settings/tokens)
   - Generate a token with **repo** permissions.

2. **Run the script**:
   ```bash
   python create_repo.py
   ```

3. **Enter your GitHub credentials when prompted**.

4. The script will:
   - Create a new repository named `contribution-graph`.
   - Make a commit with a **backdated timestamp from 1970**.
   - Push everything to GitHub automatically.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
