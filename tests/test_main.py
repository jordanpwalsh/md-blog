import os  # Added import statement for os module
import pytest
import shutil
from main import read_posts, render_posts

class TestMainFunctions:

    def setUp(self):
        self.test_directory = "tests/test_posts"
        try:
            shutil.rmtree(self.test_directory)
        except FileNotFoundError:
            os.makedirs(self.test_directory, exist_ok=True)

    def tearDown(self):
        try:
            shutil.rmtree(self.test_directory)  # Fixed the undefined name error
        except:
            pass

    def test_read_posts(self):
        # Create a sample post
        with open(os.path.join("tests/test_posts", "2024-01-25_Sample Post 1.md"), 'w', encoding='utf-8') as file:  # Fixed the undefined name error
            file.write("# Sample Post 1\nThis is the content of the first post.")

        posts = read_posts("tests/test_posts")
        print(posts[0][1])
        assert len(posts) == 2

        assert posts[0][0] == "Sample Post Title 2"
        assert "<h1>Sample Post 2</h1>" in posts[0][2]
        assert "2024-02-02" in posts[0][1]

    def test_render_posts(self):
        # Create a sample post
        with open(os.path.join("tests/test_posts", "2024-02-02_Sample Post Title 2.md"), 'w', encoding='utf-8') as file:  # Fixed the undefined name error
            file.write("# Sample Post 2\nThis is the content of the second post. Written in early February.")

        posts = read_posts("tests/test_posts")
        rendered_html = render_posts(posts)

        # Check if the HTML contains the expected structure
        print(rendered_html)
        assert "<h2>Sample Post 1</h2>" in rendered_html
        assert "<h1>Sample Post 2</h1>" in rendered_html

if __name__ == "__main__":
    pytest.main()
