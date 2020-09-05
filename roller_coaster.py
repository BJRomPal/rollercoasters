import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# load rankings data here:
dfwood = pd.read_csv(
    'C:\codeacademy\data_science\script_coaster\golden_ticket_award_winners_wood.csv')
dfwood.columns = ['Rank', 'Name', 'Park', 'Location',
                  'Supplier', 'Year_Built', 'Points', 'Year_of_Rank']
dfroller = pd.read_csv(
    'C:\codeacademy\data_science\script_coaster\\roller_coaster.csv')

#print(dfroller.head())
#print(dfwood.head())
roller_count1 = dfwood.Name.count()
dfsteel = pd.read_csv("C:\codeacademy\data_science\script_coaster\golden_ticket_award_winners_steel.csv")
dfsteel.columns = ['Rank', 'Name', 'Park', 'Location',
                   'Supplier', 'Year_Built', 'Points', 'Year_of_Rank']
#print(dfsteel.head())
roller_count2 = dfsteel.Name.count()
unique_wood_supplier = dfwood.Supplier.nunique()
unique_steel_supplier = dfsteel.Supplier.nunique()

def ranking_roller_coaster(Name, df, Park):
    roller_name = df[(df.Name == Name) & (df.Park == Park)]
    roller_name = roller_name.reset_index(drop=True)
    plt.plot(roller_name.Year_of_Rank,
             roller_name.Rank, color='red', marker='o')
    ax = plt.subplot()
    ax.set_yticks([1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
    ax.invert_yaxis()
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title('Ranking over the years for ' + Name)
    plt.show()
    return roller_name


def comparative_ranking_two_roller_coaster(Name1, Name2, df, Park1, Park2):
    roller_1 = df[(df.Name == Name1) & (df.Park == Park1)]
    roller_1 = roller_1.reset_index(drop=True)
    roller_2 = df[(df.Name == Name2) & (df.Park == Park2)]
    roller_2 = roller_2.reset_index(drop=True)
    plt.plot(roller_1.Year_of_Rank,
             roller_1.Rank, color='red', marker='o')
    plt.plot(roller_2.Year_of_Rank,
             roller_2.Rank, color='green', marker='o')
    ax = plt.subplot()
    ax.set_yticks([1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
    ax.invert_yaxis()
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title('Comparative Ranking over the years for ' + Name1 + ' and ' + Name2)
    create_legends = [Name1, Name2]
    plt.legend(create_legends, loc = 8)
    plt.show()
    return roller_1 + roller_2


def top_ranking_roller_coasters(rank_provided, df):
    ranked_coasters = df[(df.Rank <= rank_provided)]
    labels = list(name for name in ranked_coasters.Name)
    labels = list(set(labels))
    for l in labels:
        variable = ranked_coasters[(ranked_coasters.Name == l)]
        variable = variable.reset_index(drop=True)
        plt.plot(variable.Year_of_Rank, variable.Rank, marker='o')
    ax = plt.subplot()
    list_yticks = list(range(1, rank_provided + 10))
    ax.set_yticks(list_yticks)
    ax.invert_yaxis()
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title(f'Ranking of the top {rank_provided} Roller Coasters')
    plt.legend(labels, loc=8)
    plt.show()
    return df


def historigram_coasters(dataset, column_name):
    dataset_column = dataset.dropna(subset=[column_name])
    dataset_column2 = np.array(dataset_column[column_name])
    if column_name == 'height':
        plt.hist(dataset_column2, range=(0, 140), bins=40)
    else:
        plt.hist(dataset_column2, bins=40)
    plt.xlabel(column_name.capitalize())
    plt.ylabel('Number of Coasters')
    plt.title('Historigram of Coasters by ' + column_name.capitalize())
    plt.show()
    return dataset_column2

def bar_inversions_chart(dataset, amusment_park):
    plt.xlabel('Attractions in ' + amusment_park)
    plt.ylabel('Number of Inversions')
    plt.title('Number of Inversions per Attraction in ' + amusment_park)
    park_coasters = dataset[dataset['park'] == amusment_park]
    park_coasters = park_coasters.sort_values(
        'num_inversions', ascending=False)
    coaster_names = park_coasters['name']
    number_inversions = park_coasters['num_inversions']
    plt.bar(coaster_names, number_inversions)
    ax = plt.subplot()
    ax.set_xticks(list(range(len(coaster_names))))
    ax.set_xticklabels(coaster_names, rotation=30)
    plt.show()
    return number_inversions

def pie_operating_closed(dataset):
    operating = dataset[dataset.status.isin(['status.operating'])]
    closed = dataset[dataset.status.isin(['status.closed.definitely'])]
    operating_count = operating.status.count()
    closed_count = closed.status.count()
    status_list = []
    status_list.append(operating_count)
    status_list.append(closed_count)
    labels = ['Attractions operating', 'Attractions Closed']
    plt.pie(status_list, autopct='%0.2f%%', labels = labels)
    plt.axis('equal')
    plt.title('Comparative of operating and closed attractions')
    plt.show()
    return operating

def scattered_plot(dataset, column1, column2):
    dataset = dataset.dropna()
    titles = [column1, column2]
    column1_dataset = np.array(dataset[column1])
    column2_dataset = np.array(dataset[column2])
    plt.legend(titles, loc=8)
    plt.xlabel(column1.capitalize())
    plt.ylabel(column2.capitalize())
    colors = np.random.rand(1279)
    area = (30 * np.random.rand(1279))**2
    plt.scatter(column1_dataset, column2_dataset, s=area, c=colors, alpha=0.3)
    plt.show()
    return dataset

# valid_markers = ([item[0] for item in mpl.markers.MarkerStyle.markers.items() if
#                   item[1] != 'nothing' and not item[1].startswith('tick') and not item[1].startswith('caret')])
# markers = np.random.choice(valid_markers, dfwood.shape[1], replace=False)
# print(markers)

#el_toro = ranking_roller_coaster('El Toro', dfwood, 'Six Flags Great Adventure')
#el_toro_vs_bouder_dash = comparative_ranking_two_roller_coaster(
#    'El Toro', 'Boulder Dash', dfwood, 'Six Flags Great Adventure', 'Lake Compounce')
#top_5_coasters = top_ranking_roller_coasters(5, dfwood)
#speed_historigram = historigram_coasters(dfroller, 'speed')
#height_historigram = historigram_coasters(dfroller, 'height')
#length_historigram = historigram_coasters(dfroller, 'length')
#busch_gardens_tampa_bar = bar_inversions_chart(dfroller, 'Busch Gardens Tampa')
#operating_closed_pie = pie_operating_closed(dfroller)
scattered = scattered_plot(dfroller, 'height', 'speed')
