from elements.base_element import BaseElement


class Image(BaseElement):
    @property
    def type_of(self) -> str:
        return "image"

    def have_equal_dimensions(self, **kwargs):
        locator = self.get_locator(**kwargs)
        imgs_list = self.driver.find_elements(*locator)
        sizes = {(int(i.get_attribute("width")), int(i.get_attribute("height"))) for i in imgs_list}

        assert len(sizes) == 1, f"Images have different dimensions: {sizes}"
