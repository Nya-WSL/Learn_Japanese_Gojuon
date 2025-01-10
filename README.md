# Learn Japanese Gojūon

![python](https://img.shields.io/badge/Version-1.0.1-cyan) ![python](https://img.shields.io/badge/Python->=3.11.5,<3.14-blue) ![NiceGUI](https://img.shields.io/badge/NiceGUI-2.9.0-blue) ![os](https://img.shields.io/badge/OS-Windows|Linux|MacOS-orange)

### Build

```
# use poetry (min size)
pip install poetry
poetry install
poetry run python build.py --name Project_Name --icon icon.ico --windowed n2n_client.py

例：poetry run python build.py --name Learn_Japanese_Gojūon --icon logo.ico --windowed main.py
```

#### Linux Server Build

```
# Linux Desktop：无需修改，参考Build
# Linux Server：修改 ui.run() 中的 native=True 为 native=False
# 只能通过 http://localhost:port 访问
# 如通过局域网访问或无法访问，可能需要在 ui.run() 中新增参数：host="0.0.0.0"

pip install poetry # or pip3 install poetry
poetry install
poetry run python build.py --name Project_Name --icon icon.ico --windowed n2n_client.py
```

### Usage

#### Linux

- 已编译
    - `./Learn_Japanese_Gojūon`
    
- 未编译

    - ```
      pip3 install poetry
      poetry install
      ```

    - `poetry run python3 main.py`

    or

    - ```
      pip install poetry
      poetry install
      ```

    - ` poetry run python main.py`

#### MacOS

- 已编译
    - Mac编译需自行解决签名和公证，建议不编译直接运行
    - 参考 [Build](#Build)
    
- 未编译

    - ```
      pip3 install poetry
      poetry install
      ```

    - `poetry run python3 main.py`

    or

    - ```
      pip install poetry
      poetry install
      ```

    - ` poetry run python main.py`

# 联系我们

- [提交issues](https://github.com/Nya-WSL/Learn_Japanese_Gojuon/issues)

- [support@nya-wsl.com](mailto:support@nya-wsl.com)

- [Nya-WSL服务维护与反馈群](https://jq.qq.com/?_wv=1027&k=tSeB0sdy)