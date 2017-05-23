from datetime import date
import random
import sys

start_date = date.today().replace(day=1, month=1).toordinal()
end_date = date.today().replace(day=31, month=12).toordinal()

loremipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit.
""".split()

def random_cancelled():
    return random.choice(["true", "false"])

def random_content():
    n = random.randint(1, len(loremipsum) - 1)
    return " ".join(random.sample(loremipsum, n))

def random_date():
    return date.fromordinal(random.randint(start_date, end_date))

def random_title():
    return " ".join(random.sample(loremipsum, random.randint(1, 7)))

def random_type():
    return random.choice(["event", "meeting"])

def write_file(file_name, day):
    f = open(file_name, "w")

    #front-matter
    f.write("---\n")
    f.write("date: {}\n".format(day))
    f.write("type: {}\n".format(random_type()))
    f.write("cancelled: {}\n".format(random_cancelled()))
    f.write("title: {}\n".format(random_title()))
    f.write("---\n")

    #content
    f.write(random_content())

    f.close()

def main(iters):
    for i in range(iters):
        day = random_date()
        file_name = str(i) + "-" + str(day) + ".md"
        write_file(file_name, day)

if __name__ == '__main__':
    iters = int(sys.argv[1])
    main(iters)
