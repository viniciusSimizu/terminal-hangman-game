# Terminal Hangman

## Usage
```bash
git clone https://github.com/viniciusSimizu/terminal-hangman-game.git
```

```bash
cd terminal-hangman-game
```

### Python 3.10.x+
```bash
python main.py
```

### Docker
```bash
docker build -t hangman .
```

```bash
docker run -it --rm --name hangman -v "$PWD":/usr/src/app -w /usr/src/app hangman
```
