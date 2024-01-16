from freq.app import App
from freq.wave import Wave


def main():
    app = App()
    app.content.add_wave(Wave(0.1, 100, 0))
    app.content.add_wave(Wave(0.3, 10, 0))
    app.run()


if __name__ == "__main__":
    main()
