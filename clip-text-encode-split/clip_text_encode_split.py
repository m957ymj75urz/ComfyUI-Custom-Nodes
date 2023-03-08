class RawText:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"raw_text": ("STRING", {"multiline": True})}}
    
    RETURN_TYPES = ("RAW_TEXT",)
    FUNCTION = "forward"
    CATEGORY = "conditioning"

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

NODE_CLASS_MAPPINGS = {
    "RawText": RawText,
    "RawTextEncode": RawTextCLIPEncode
}