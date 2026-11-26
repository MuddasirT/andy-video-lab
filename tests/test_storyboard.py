import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class StoryboardTests(unittest.TestCase):
    def test_episode_has_six_scenes_and_30_seconds(self):
        doc = json.loads((ROOT / "projects/tinytoon_planet/episode_01.json").read_text())
        self.assertEqual(len(doc["scenes"]), 6)
        self.assertEqual(sum(x["duration_seconds"] for x in doc["scenes"]), 30)

    def test_scenes_include_narration(self):
        doc = json.loads((ROOT / "projects/tinytoon_planet/episode_01.json").read_text())
        self.assertTrue(all(x["narration"] and x["description"] for x in doc["scenes"]))


if __name__ == "__main__":
    unittest.main()
