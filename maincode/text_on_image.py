from PIL import Image, ImageDraw, ImageFont
import config

def line_to_lines(text):
    new_text = ""
    limit = 53
    while len(text):
        if len(text) >= limit:
            if text[limit] != " ":
                new_index = text[0:limit].rfind(" ")
                new_text += text[0:new_index] + '\n'
                text = text[new_index + 1:]
            elif text[limit] == " ":
                new_text += text[0:limit] + '\n'
                text = text[limit + 1:]
        else:
            new_text += text
            break
    return new_text

def text_on_image_(user_id, buy_or_sell, seed_type, seed_descr, contact):
  original = Image.open(config.seeds_photo[seed_type])
  idraw = ImageDraw.Draw(original)
  
  idraw.text((850, 160), buy_or_sell, font=config.head_font)
  idraw.text((850, 210), seed_type, font=config.head_font)
  idraw.text((210, 280), line_to_lines(seed_descr), font=config.main_font)
  idraw.text((210, 780), line_to_lines(contact), font=config.main_font)

  tm_text = "@KSM"
  idraw.text((0, 1020), tm_text, font=config.main_font, fill=(64, 64, 64))
  result_ = "newcontent/" + str(user_id) + ".png"
  print(result_)
  original.save(result_)

  return result_
  