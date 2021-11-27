import json

with open('courses.json') as f:
    courses = json.load(f)

majors = courses['majors']

colors = ['red', 'orange', 'amber', 'yellow', 'lime', 'green', 'emerald', 'teal', 'cyan', 'sky', 'blue', 'indigo', 'violet', 'purple', 'fuchsia', 'pink', 'rose']

cur_color = 0
for major in majors:
    courses['majors'][major]['color'] = colors[cur_color]
    cur_color += 1
    if cur_color == len(colors):
        cur_color = 0

courses['majors'] = majors

with open('courses.json', 'w') as out:
    json.dump(courses, out, indent=4)