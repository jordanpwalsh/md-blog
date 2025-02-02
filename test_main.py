import pytest
from main import read_posts, render_posts

class TestMainFunctions:

    def setUp(self):
        self.test_directory = "tests/test_posts"
        os.makedirs(self.test_directory, exist_ok=True)

    def tearDown(self):
        for filename in os.listdir(self.test_directory):
            if filename.endswith(".md"):
                os.remove(os.path.join(self.test_directory, filename))
        os.rmdir(self.test_directory)

    def test_read_posts(self):
        # Create a sample post
        with open(os.path.join("tests/test_posts", "sample1.md"), 'w', encoding='utf-8') as file:
            file.write("# Sample Post 1\nThis is the content of the first post.")

        posts = read_posts("tests/test_posts")
        assert len(posts) == 1
        assert posts[0][0] == "sample1"
        assert "<h1>Sample Post 1</h1>" in posts[0][1]

    def test_render_posts(self):
        # Create a sample post
        with open(os.path.join("tests/test_posts", "sample2.md"), 'w', encoding='utf-8') as file:
            file.write("# Sample Post 2\nThis is the content of the second post.")

        posts = read_posts("tests/test_posts")
        rendered_html = render_posts(posts)
        
        # Check if the HTML contains the expected structure
        assert "<h2>sample2</h2>" in rendered_html
        assert "<div><h1>Sample Post 2</h1>This is the content of the second post.</div>" in rendered_html

if __name__ == "__main__":
    pytest.main()
