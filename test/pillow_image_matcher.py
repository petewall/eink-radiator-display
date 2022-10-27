"""A special hamcrest matcher for matching Pillow images"""

from hamcrest.core.base_matcher import BaseMatcher

class PillowImageMatcher(BaseMatcher):
    """A special hamcrest matcher for matching Pillow images"""

    def __init__(self, image):
        self.image = image

    def _matches(self, item):
        """Returns true if the image bytes are the same"""
        return self.image.tobytes() == item.tobytes()

    def describe_to(self, description):
        """Provides an description for the object"""
        description.append_text(f'an image matching {self.image}')

def the_same_image_as(image):
    """An human-readable function for creating the matcher"""
    return PillowImageMatcher(image)
