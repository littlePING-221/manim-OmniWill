from manimlib import *

def FadeUpTransform(mob, target_mob):
    return AnimationGroup(FadeOut(mob, UP*0.5), FadeIn(target_mob, UP*0.5))

def make_abbr_full_mobj(abbr: str, full: str):
    abbr_pat = [f"{{\LARGE {c}}}" for c in full if c in abbr]
    full_tex = "".join([f"{{\LARGE {c}}}" if c in abbr else c for c in full])
    full_text = TexText(full_tex, color=GREY, tex_to_color_map={key: WHITE for key in abbr_pat})
    abbr_text = VGroup()
    # 用于跟踪每个大写字母的索引
    abbr_indices = {c: 0 for c in abbr}

    for c in abbr_pat:
        index = abbr_indices[c[-2]]  # 获取当前字母的索引
        abbr_indices[c[-2]] += 1  # 更新字典中的索引值
        t = full_text.select_part(c, index)  # 使用索引选择对应的部分
        abbr_text.add(t.copy())
        full_text.remove(t)
    abbr_text.save_state()
    abbr_text.arrange(buff=0.1)
    return abbr_text, full_text

def Abbr2Full(s: Scene, abbr: str, full: str):
    abbr_text, full_text = make_abbr_full_mobj(abbr, full)
    s.play(Write(abbr_text))
    s.wait()
    s.play(abbr_text.animate.restore())
    s.play(Write(full_text))
    s.remove(abbr_text)
    return full_text


def Abbr2Full2Abbr(s: Scene, abbr: str, full: str):
    abbr_text, full_text = make_abbr_full_mobj(abbr, full)
    abbr_state = abbr_text.copy()
    s.play(Write(abbr_text))
    s.wait()
    s.play(abbr_text.animate.restore())
    s.play(Write(full_text))
    s.wait()
    s.play(Uncreate(full_text))
    abbr_text.saved_state = abbr_state
    return abbr_text