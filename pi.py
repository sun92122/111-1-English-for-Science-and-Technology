import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

PATH = 'pi_10M'  # 'pi_10M' (10M) or 'pi_1B' (1B)
pi = ''
REPEAT = False
DELAY = 10  # (ms)
word_to_find = '101010101'  # to change
word_to_find_width = 3  # to change


def PI():
    global pi
    try:
        with open(PATH) as f:
            pi = f.read()
    except:
        print(f'{PATH} not found.')
        return


def str_to_2dlist(string):
    global word_to_find_width, word_to_find_hight, len_to_find
    tmp_list = list(string)
    tmp_list = np.array(tmp_list, dtype=float)
    tmp_list.resize([word_to_find_hight, word_to_find_width])
    return tmp_list


if __name__ == '__main__':
    PI()
    print('pi loaded.\nto find: ', word_to_find)
    len_to_find = len(word_to_find)
    word_to_find_hight = len_to_find//word_to_find_width
    len_pi = len(pi)

    fig = plt.figure()

    ax = plt.subplot2grid((3, 3), (1, 1), rowspan=2, colspan=2)
    ax1 = plt.subplot2grid((3, 3), (0, 0))
    ax2 = plt.subplot2grid((3, 3), (0, 1))

    ax.axis('off')
    ax1.axis('off')
    ax2.axis('off')
    ys = str_to_2dlist(pi[0:len_to_find])
    img = ax.imshow(ys, cmap='gray', vmin=0, vmax=1)
    list_to_find = str_to_2dlist(word_to_find)
    print(list_to_find)
    ytext = ax2.text(-0.5, 0.4, '0')
    ax1.imshow(list_to_find, cmap='gray', vmin=0, vmax=1)
    ax2.imshow([[1]], cmap='gray', vmin=0, vmax=1)

    def update(counter):
        start = word_to_find_width*counter
        ys = np.array(str_to_2dlist(
            pi[start:start*word_to_find_width+len_to_find]))
        img.set_data(ys)
        ytext.set_text(start)
        return img, ytext

    for i in np.arange(len_pi//word_to_find_width):
        if pi[i*word_to_find_width:i*word_to_find_width+len_to_find] == word_to_find:
            end = i + 1
            break
        elif i % 1000 == 0 and i:
            print("i =", i*word_to_find_width, "not found")
    else:
        print(word_to_find, f"not found in {PATH}")
        end = len_pi//word_to_find_width

    print((end-1)*word_to_find_width)

    ani = FuncAnimation(fig, update, interval=DELAY, blit=True,
                        frames=np.arange(0, end), repeat=REPEAT)

    plt.show()