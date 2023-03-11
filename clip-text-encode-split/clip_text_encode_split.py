class RawText:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"raw_text": ("STRING", {"multiline": True})}}
    
    RETURN_TYPES = ("RAW_TEXT",)
    FUNCTION = "forward"
    CATEGORY = "utils"

    def forward(self, raw_text):
        return (raw_text, )
    
class RawTextCLIPEncode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"raw_text": ("RAW_TEXT", ), 
                             "clip": ("CLIP", )
                }}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "conditioning"

    def encode(self, clip, raw_text):
        return ([[clip.encode(raw_text), {}]], )
    
class RawTextCombine:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "raw_text_1": ("RAW_TEXT", ), 
                "raw_text_2": ("RAW_TEXT", )
            }
        }
    RETURN_TYPES = ("RAW_TEXT",)
    FUNCTION = "combine"

    CATEGORY = "utils"

    def combine(self, raw_text_1, raw_text_2):
        return (raw_text_1 + "," + raw_text_2, )
    
class RawTextReplace:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "search": ("STRING", {}),
                "subject": ("RAW_TEXT", ), 
                "replace": ("RAW_TEXT", )
            }
        }
    RETURN_TYPES = ("RAW_TEXT",)
    FUNCTION = "replace"

    CATEGORY = "utils"

    def replace(self, search, subject, replace):
        return (subject.replace(search, replace), )

NODE_CLASS_MAPPINGS = {
    "RawText": RawText,
    "RawTextEncode": RawTextCLIPEncode,
    "RawTextCombine": RawTextCombine,
    "RawTextReplace": RawTextReplace
}