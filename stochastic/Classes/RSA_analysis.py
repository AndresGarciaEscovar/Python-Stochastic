""" Contains the class to simulate random sequential adsorption with nearest
    neighbor exclusion for a periodic lattice.
"""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Imports: General.
import copy as cp
import numpy as np

from dataclasses import dataclass
from matplotlib import pyplot as plt


# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------


class RSAResultsAnalysis:
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
                # A new data frame is produced.
                if line0[0][0] == "-":
                    # Append the data frame.
                    data_frames0.append(cp.deepcopy(tmp_list0))

                    # Empty the temporary data frame.
                    tmp_list0 = []

                    continue

                # Append thes line.
                tmp_list0.append(line0)

            return data_frames0

        # //////////////////////////////////////////////////////////////////////
        # Implementation.
        # //////////////////////////////////////////////////////////////////////

        # Import the data.
        data = []
        with open(file_path, "r") as fl:
            lines = fl.readlines()

            # Get each line.
            for line in lines:
                # Split the data.
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

            plt.suptitle(plot_title, fontsize=12)

            xticks_minor = [k + 0.5 for k, _ in enumerate(configurations[0])]
            axis.set_xticks([k + 1 for k, _ in enumerate(configurations[0])], minor=False)
            axis.set_xticks(xticks_minor, minor=True)

            yticks_minor = [(times[j] + times[j + 1]) / 2.0 for j in range(len(times) - 1)]
            axis.set_yticks(times, minor=False)
            axis.set_yticks(yticks_minor, minor=True)

            axis.set_xlim(xticks_minor[0], xticks_minor[-1] + 1.0)
            axis.set_ylim(-0.05, max(times) + 0.1)
            axis.xaxis.grid(True, which='minor')

            axis.spines['left'].set_position(('data', xticks_minor[0]))
            axis.spines['right'].set_position(('data', xticks_minor[-1] + 1.0))

            axis.set_xlabel('Site Number')
            axis.set_ylabel('Elapsed Simulation Time')

        plt.tight_layout()
        plt.show()
