""" Contains the class for results analysis of the different simulation types.
"""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Imports: General.
import copy as cp
import numpy as np

from matplotlib import pyplot as plt

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------


class RSA1DResultsAnalysis:
    """ Class that contains the functions to plot the results.
    """

    @staticmethod
    def plot_results(file_path: str):
        """ Given the files with the results, plots the results of the
            simulation.

            :param file_path: The path of the file where the results are stored.
        """

        # Get the data.
        data = []
        with open(file_path, "r") as fl:
            lines = fl.readlines()
            for line in lines:
                data.append(line.split(","))

        # Format the basic features.
        plot_title = ", ".join(list(map(lambda x: x.strip(), data[0])))
        axis_names = list(map(lambda x: x.strip(), data[1]))
        data = np.array(data[2:], dtype=float)
        xmax = max(data[:, 0])
        
        # New figure.
        fig, axes = plt.subplots(2, 2)
        plt.suptitle(plot_title, fontsize=6)

        # Format the graph of the data for the success/n vs attemps/n.
        axes[0][0].plot(data[:, 0], data[:, 1])
        axes[0][0].spines['left'].set_position('zero')
        axes[0][0].spines['bottom'].set_position('zero')
        axes[0][0].set_xlim(0, xmax)
        axes[0][0].set_ylim(0, 1.0)
        axes[0][0].set_xlabel(axis_names[0])
        axes[0][0].set_ylabel(axis_names[1])

        # Format the graph of the data for the singlets/n vs attemps/n.
        axes[0][1].plot(data[:, 0], data[:, 2])
        axes[0][1].spines['left'].set_position('zero')
        axes[0][1].spines['bottom'].set_position('zero')
        axes[0][1].set_xlim(0, xmax)
        axes[0][1].set_ylim(0, 1.0)
        axes[0][1].set_xlabel(axis_names[0])
        axes[0][1].set_ylabel(axis_names[2])

        # Format the graph of the data for the doublets/n vs attemps/n.
        axes[1][0].plot(data[:, 0], data[:, 3])
        axes[1][0].spines['left'].set_position('zero')
        axes[1][0].spines['bottom'].set_position('zero')
        axes[1][0].set_xlim(0, xmax)
        axes[1][0].set_ylim(0, 1.0)
        axes[1][0].set_xlabel(axis_names[0])
        axes[1][0].set_ylabel(axis_names[3])

        # Format the graph of the data for the triplets/n vs attemps/n.
        axes[1][1].plot(data[:, 0], data[:, 4])
        axes[1][1].spines['left'].set_position('zero')
        axes[1][1].spines['bottom'].set_position('zero')
        axes[1][1].set_xlim(0, xmax)
        axes[1][1].set_ylim(0, 1.0)
        axes[1][1].set_xlabel(axis_names[0])
        axes[1][1].set_ylabel(axis_names[4])

        # Finish formatting the figure.
        plt.tight_layout()
        file_path = ".".join(file_path.split(".")[:-1]) + ".png"

        # Save the figure.
        plt.savefig(file_path)

    @staticmethod
    def plot_lattices(file_path: str):
        """ Plots the lattices configuration from the configuration folder.
        """

        # //////////////////////////////////////////////////////////////////////
        # Auxiliary functions.
        # //////////////////////////////////////////////////////////////////////

        def get_data_frames(data0: list) -> list:
            """ Splits the data into individual data frames and returns the list
                of the data frames.

                :param data0: The data to be split into different data frames.

                :return: The data to be split into the data frames.
            """

            # Create an empty list.
            data_frames0 = []

            # List where the data can be stored.
            tmp_list0 = []

            # Scan the data frame.
            for i0, line0 in enumerate(data0):
                if line0[0][0] == "-":
                    data_frames0.append(cp.deepcopy(tmp_list0))
                    tmp_list0 = []
                    continue

                tmp_list0.append(line0)

            return data_frames0

        # //////////////////////////////////////////////////////////////////////
        # Implementation.
        # //////////////////////////////////////////////////////////////////////

        # Import the data.
        data = []
        with open(file_path, "r") as fl:
            lines = fl.readlines()
            for line in lines:
                data.append(line.split(","))

        # Change the data to individual data frames.
        data = get_data_frames(data)
        for i, frame in enumerate(data):
            plot_title = ", ".join(frame[0])
            frame_data = np.array(frame[2:][:], dtype=float)
            times = frame_data[:, 0]
            configurations = frame_data[:, 1:]

            fig, axis = plt.subplots(nrows=1)
            for j, configuration in enumerate(configurations):
                x_placement = [1.0 * (k + 1) for k, particle in enumerate(configuration) if not particle == 0.0]
                y_placement = [times[j] for _ in x_placement]
                axis.scatter(x_placement, y_placement, s=10)

            plt.suptitle(plot_title, fontsize=6)

            xticks_minor = [k + 0.5 for k, _ in enumerate(configurations[0])]
            axis.set_xticks([k + 1 for k, _ in enumerate(configurations[0])], minor=False)
            axis.set_xticks(xticks_minor, minor=True)

            yticks_minor = [(times[j] + times[j + 1]) / 2.0 for j in range(len(times) - 1)]
            axis.set_yticks(times, minor=False)
            axis.set_yticks(yticks_minor, minor=True)
            axis.yaxis.grid(True, which='minor')

            axis.set_xlim(xticks_minor[0], xticks_minor[-1] + 1.0)
            axis.set_ylim(-0.05, max(times) + 0.1)
            axis.xaxis.grid(True, which='minor')

            axis.spines['left'].set_position(('data', xticks_minor[0]))
            axis.spines['right'].set_position(('data', xticks_minor[-1] + 1.0))

            axis.set_xlabel('Site Number')
            axis.set_ylabel('Elapsed Simulation Time')

            file_path_ = file_path.split(".")
            extension = ".png"
            file_path_ = "".join([".".join(file_path_[:-1]), f"-frame_{i}", extension])

            plt.tight_layout()
            plt.savefig(file_path_)
            plt.close(fig)


class RSA2DResultsAnalysis:
    """ Class that contains the functions to plot the results.
    """

    @staticmethod
    def plot_results(file_path: str):
        """ Given the files with the results, plots the results of the
            simulation.

            :param file_path: The path of the file where the results are stored.
        """

        # Get the data.
        data = []
        with open(file_path, "r") as fl:
            lines = fl.readlines()
            for line in lines:
                data.append(line.split(","))

        # Format the basic features.
        plot_title = ", ".join(list(map(lambda x: x.strip(), data[0])))
        axis_names = list(map(lambda x: x.strip(), data[1]))
        data = np.array(data[2:], dtype=float)
        xmax = max(data[:, 0])

        # New figure.
        fig, axes = plt.subplots(ncols=1, nrows=2)
        plt.suptitle(plot_title, fontsize=6)

        # Format the graph of the data for the success/n vs attemps/n.
        axes[0].plot(data[:, 0], data[:, 1])
        axes[0].spines['left'].set_position('zero')
        axes[0].spines['bottom'].set_position('zero')
        axes[0].set_xlim(0, xmax)
        axes[0].set_ylim(0, 1.0)
        axes[0].set_xlabel(axis_names[0])
        axes[0].set_ylabel(axis_names[1])

        # Format the graph of the data for the coverage/n vs attemps/n.
        axes[1].plot(data[:, 0], data[:, 2])
        axes[1].spines['left'].set_position('zero')
        axes[1].spines['bottom'].set_position('zero')
        axes[1].set_xlim(0, xmax)
        axes[1].set_ylim(0, 1.0)
        axes[1].set_xlabel(axis_names[0])
        axes[1].set_ylabel(axis_names[2])

        # Finish formatting the figure.
        plt.tight_layout()
        file_path = ".".join(file_path.split(".")[:-1]) + ".png"

        # Save the figure.
        plt.savefig(file_path)

    @staticmethod
    def plot_lattices(file_path: str):
        """ Plots the lattices configuration from the configuration folder.
        """

        # //////////////////////////////////////////////////////////////////////
        # Auxiliary functions.
        # //////////////////////////////////////////////////////////////////////

        def get_data_frames(data0: list) -> list:
            """ Splits the data into individual data frames and returns the list
                of the data frames.

                :param data0: The data to be split into different data frames.

                :return: The data to be split into the data frames.
            """

            data_frames0 = []
            tmp_list0 = []
            for i0, line0 in enumerate(data0):
                if line0[0][0] == "-":
                    data_frames0.append(cp.deepcopy(tmp_list0))
                    tmp_list0 = []
                    continue

                tmp_list0.append(line0)

            return data_frames0

        # //////////////////////////////////////////////////////////////////////
        # Implementation.
        # //////////////////////////////////////////////////////////////////////

        # Import the data.
        data = []
        with open(file_path, "r") as fl:
            lines = fl.readlines()
            for line in lines:
                data.append(line.split(","))

        # Change the data to individual data frames.
        data = get_data_frames(data)

        for i, frame in enumerate(data):
            times = [time[0] for time in frame[2:]]
            indexes_list = [indexes for indexes in frame[1][1:]]

            for j, indexes in enumerate(indexes_list):
                indexes = indexes.split("x")
                indexes_list[j] = [int(indexes[0].strip("(")), int(indexes[1].strip(")\n"))]

            indexes_x = [indexes[0] for indexes in indexes_list]
            indexes_y = [indexes[1] for indexes in indexes_list]

            frame_data = []
            for row in frame[2:]:
                row = map(int, row[1:])
                frame_data.append(cp.deepcopy(list(row)))

            for j, time in enumerate(times):
                row = frame_data[j]
                x_placement = [1 * (indexes_x[k] + 1) for k, particles in enumerate(row) if particles == 1]
                y_placement = [1 * (indexes_y[k] + 1) for k, particles in enumerate(row) if particles == 1]

                coverage = len(x_placement) / len(row)

                fig, axis = plt.subplots(nrows=1)
                axis.scatter(x_placement, y_placement, s=12)

                plot_title = ", ".join(frame[0])
                plot_title = ", ".join([plot_title, f"Elapsed Time: {time}", f"Coverage = {coverage:.5f}"])
                plt.suptitle(plot_title, fontsize=6)

                xticks_minor = [k + 0.5 for k in indexes_x]
                axis.set_xticks([k + 1 for k in indexes_x], minor=False)
                axis.set_xticks(xticks_minor, minor=True)

                yticks_minor = [k + 0.5 for k in indexes_y]
                axis.set_yticks([k + 1 for k in indexes_y], minor=False)
                axis.set_yticks(yticks_minor, minor=True)

                axis.set_xlim(xticks_minor[0], xticks_minor[-1] + 1.0)
                axis.set_ylim(yticks_minor[0], yticks_minor[-1] + 1.0)
                axis.xaxis.grid(True, which='minor')
                axis.yaxis.grid(True, which='minor')

                axis.spines['left'].set_position(('data', xticks_minor[0]))
                axis.spines['right'].set_position(('data', xticks_minor[-1] + 1.0))
                axis.spines['bottom'].set_position(('data', yticks_minor[0]))
                axis.spines['top'].set_position(('data', yticks_minor[-1] + 1.0))

                axis.set_xlabel('x index')
                axis.set_ylabel('y index')

                file_path_ = file_path.split(".")
                extension = ".png"
                file_path_ = "".join([".".join(file_path_[:-1]), f"-frame_{i}-{j}", extension])

                plt.tight_layout()
                plt.savefig(file_path_)
                plt.close(fig)
