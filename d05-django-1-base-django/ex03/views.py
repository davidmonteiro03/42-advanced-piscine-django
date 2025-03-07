from django.shortcuts import render

# Create your views here.
def index(request):
    colors = {'noir': "ffffff",
              'rouge': "ff0000",
              'bleu': "0000ff",
              'vert': "00ff00"}
    shd_fac = 50
    rgb_cnt, nil_cnt = 1, shd_fac
    lines = []
    for _ in range(shd_fac):
        shade = []
        for k, v in colors.items():
            fac = nil_cnt if k == 'noir' else rgb_cnt
            r, g, b = v[:2], v[2:4], v[4:6]
            r, g, b = int(r, 16), int(g, 16), int(b, 16)
            r, g, b = int(r * (fac / shd_fac)), \
                int(g * (fac / shd_fac)), int(b * (fac / shd_fac))
            r, g, b = hex(r).removeprefix('0x'), hex(g).removeprefix('0x'), hex(b).removeprefix('0x')
            shade.append({'color': f"#{r:>02}{g:>02}{b:>02}"})
        lines.append(shade)
        rgb_cnt += 1
        nil_cnt -= 1
    return render(request,
                  'ex03/index.html',
                  context={'colors': colors.keys(),
                           'lines': lines})
