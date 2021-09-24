import cv2
import sys
import fire
import os
from loguru import logger


def flip_img(img, text="LIOR"):
    flipVertical = cv2.flip(img, 0)

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 10
    color = (0, 0, 0)
    thickness = 5
    lineType = cv2.LINE_AA

    textsize = cv2.getTextSize(text, font, fontScale, thickness)[0]
    h, w, _ = flipVertical.shape
    org = (int(w / 2 - textsize[0] / 2), int(h / 2 + textsize[1] / 2))

    img_with_text = cv2.putText(flipVertical, text, org, font, fontScale,
                                color, thickness, lineType)
    return img_with_text


def flip_cli(src_path,
             text="LIOR",
             inter=False,
             dest_path=None,
             dest_suff=None,
             dbgout=False):
    """ Use --inter for show
    """
    from pathlib import Path
    img = cv2.imread(src_path)
    if img is None:
        raise Exception(f"file not found {src_path}")
    logger.info(f"loaded={src_path}")
    img_with_text = flip_img(img, text=text)
    if dbgout:
        dest_suff = ".flip._out.jpg"

    if inter:
        cv2.imshow('flipped image with text', img_with_text)
        cv2.waitKey(0)
    elif dest_path:
        cv2.imwrite(dest_path, img_with_text)
    elif dest_suff:
        res_path = src_path + dest_suff
        cv2.imwrite(os.path.join(res_path), img_with_text)
    else:
        logger.warning(f"no out provided. size {img_with_text.shape[:2]}")


def main_():
    import fire
    fire.Fire(flip_cli)


if __name__ == '__main__':
    main_()