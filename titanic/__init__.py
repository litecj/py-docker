from titanic.template.plot import Plot

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1. Visualization 2. Modeling 3. Machine Learning 4. Machine Release')
        if menu == '0':
            break
        elif menu == '1':
            plot = Plot()
            plot.show_draw_survived_dead()
            # plot.show_draw_survived_dead2()
        elif menu == '2':
            plot = Plot()
            # plot.show_plot_pclass()
            # plot.show_plot_embarked()
            plot.show_plot_sex2()
        elif menu == '3':
            plot = Plot()
            plot.show_plot_sex()