import os
import sys

sys.path.append(os.path.dirname(__name__))

from cv_maker import create_app

app = create_app()


if __name__ == '__main__':
    app.run()
