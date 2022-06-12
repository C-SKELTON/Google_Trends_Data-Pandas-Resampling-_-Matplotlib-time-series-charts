import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_tesla.head(5)
df_tesla.shape

df_tesla.TSLA_WEB_SEARCH.max()
df_tesla.TSLA_WEB_SEARCH.min()

df_tesla.describe()

df_unemployment_19 = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
df_unemployment_19.head(5)
df_unemployment_19.shape

df_unemployment_20 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')

df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_btc_price.head(2)

df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_search.shape
df_btc_search.head(2)


df_tesla.isna().values.any()
df_unemployment_19.isna().values.any()
df_btc_price.isna().values.any()
df_btc_search.isna().values.any()


df_btc_price[df_btc_price.CLOSE.isna()]
df_btc_price.dropna(inplace=True)

# print(df_btc_price.dtypes)
# print(df_btc_search.dtypes)
# print(df_tesla.dtypes)
# print(df_unemployment_19.dtypes)

df_btc_price.DATE =pd.to_datetime(df_btc_price.DATE)
df_btc_search.MONTH=pd.to_datetime(df_btc_search.MONTH)
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_unemployment_19.MONTH = pd.to_datetime(df_unemployment_19.MONTH)
df_unemployment_20.MONTH = pd.to_datetime(df_unemployment_20.MONTH)


df_tesla.MONTH.head()

#grabs the month end prices 
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
df_btc_monthly.head(5)

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

plt.figure(figsize=(10,6), dpi=120)
plt.xticks(fontsize=14, rotation = 45)
ax1 = plt.gca()
ax2 = ax1.twinx()

plt.title('Tesla Web Search vs Price', fontsize=18)
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=16)
ax2.set_ylabel('Search Trend', color='#7393B3', fontsize=16)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])



ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, '#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, '#7393B3', linewidth=3)
plt.show()




plt.figure(figsize=(10,6), dpi=120)
plt.xticks(fontsize=14, rotation = 45)
ax1 = plt.gca()
ax2 = ax1.twinx()

plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
ax1.set_ylabel('BTC Price', color='#E858D9', fontsize=16)
ax2.set_ylabel('Search Trend', color='#F08F2E', fontsize=16)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax2.set_ylim(bottom=0, top=15000)
ax2.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])


ax1.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH, '#E858D9', linewidth=3, marker='o')
ax2.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, '#F08F2E', linewidth=3, linestyle='--')
plt.show()



plt.figure(figsize=(10,6), dpi=120)
plt.xticks(fontsize=14, rotation = 45)
ax1 = plt.gca()
ax2 = ax1.twinx()

plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
ax2.set_ylabel('UE_BENEFITS_WEB_SEARCH', color='#E8CB58', fontsize=16)
ax1.set_ylabel('FRED U/E Rate', color='#40D494', fontsize=16)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

# ax1.set_xlabel('Month')

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment_19.MONTH.min(), df_unemployment_19.MONTH.max()])

ax1.grid(color='grey', linestyle='--')

roll_df = df_unemployment_19[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()

ax1.plot(df_unemployment_19.MONTH, df_unemployment_19.UNRATE, '#40D494', linewidth=3, linestyle='--' )
ax2.plot(df_unemployment_19.MONTH, df_unemployment_19.UE_BENEFITS_WEB_SEARCH, '#E8CB58', linewidth=3 )

plt.figure(figsize=(10,6), dpi=120)
plt.xticks(fontsize=14, rotation = 45)
ax1 = plt.gca()
ax2 = ax1.twinx()

plt.title('Rolling Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
ax2.set_ylabel('UE_BENEFITS_WEB_SEARCH', color='green', fontsize=16)
ax1.set_ylabel('FRED U/E Rate', color='blue', fontsize=16)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment_19.MONTH.min(), df_unemployment_19.MONTH.max()])

ax1.plot(df_unemployment_19.MONTH, roll_df.UNRATE, 'blue', linewidth=3, linestyle='-.' )
ax2.plot(df_unemployment_19.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'green', linewidth=3, linestyle = 'dotted')


plt.show()

plt.figure(figsize=(10,6), dpi=120)
plt.xticks(fontsize=14, rotation = 45)
ax1 = plt.gca()
ax2 = ax1.twinx()

plt.title('Monthly "Unemployment Benefits" Web Search vs UNRATE including 2020', fontsize=18)
ax2.set_ylabel('UE_BENEFITS_WEB_SEARCH', color='#71315B', fontsize=16)
ax1.set_ylabel('FRED U/E Rate', color='#0C81A0', fontsize=16)
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)

# ax1.set_ylim(bottom=3, top=10.5)

ax1.set_xlim([df_unemployment_20.MONTH.min(), df_unemployment_20.MONTH.max()])

ax1.plot(df_unemployment_20.MONTH, df_unemployment_20.UNRATE, '#0C81A0', linewidth=3, linestyle='-.' )
ax2.plot(df_unemployment_20.MONTH, df_unemployment_20.UE_BENEFITS_WEB_SEARCH, '#71315B', linewidth=3, linestyle = 'dotted')


