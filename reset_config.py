with open("amber/config.json", 'w') as f:
	f.write("""{
    "COLOR": "",
    "PREFIX": "",
    "TOKEN": "",
    "plugins": {
        "algebra": {
            "path": "plugins/algebra.py"
        },
        "graph": {
            "density": 500,
             "scale": {
                 "x": 10,
                 "y": 10
            }
        },
        "8ball": {
            "path": "plugins/eightball.py"
        },
        "about": {
            "path": "plugins/about.py"
        },
        "hello": {
            "path": "plugins/hello.py"
        },
        "help": {
            "commands": {
                "8ball": "Fortunes and advice",
                "about": "General information",
                "hello": "Amber says hello",
                "help": "Displays this message"
            },
            "path": "plugins/help.py"
        }
    },
    "tools": {
        "ocr": {
             "path": "tools/ocr.py",
             "tesseract_path": ""
        }
    }
}""")
