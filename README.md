# gemini

Google Gemini Examples

## How to use

First, ensure that python3.9 is installed in your environment. Then you can install the project as the following steps:

```zsh
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install --upgrade pip
$ pip3 install -r requirements.txt
```

You should remove .env.example as .env, and modify `GOOGLE_API_KEY` and `PORT` as your own

```zsh
$ mv .env.example .env
```

Last, you should run the examples as following:

```zsh
$ python3 text.py
```

## License

This project is licensed under the MIT License.
