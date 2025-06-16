from ..config import Config


class FontManager:
    def __init__(self, base_font_path):
        """
        Initializes the font manager.
        Args:
            base_fonts_path (str) = path containing .tff/.otf files.
        """
        self.base_fonts_path = base_font_path
        self.loaded_fonts = {}

    def load_font(self, alias, filname, size) -> None:
        """

        """
        if alias in self.loaded_fonts:
            pass


    def get_font(self) -> None:
        """
        
        """
        pass
