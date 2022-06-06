{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afe5544c-3811-4ff0-93d6-7fb25b7efcac",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from os import path\n",
    "import pandas as pd\n",
    "import time\n",
    "start = time.time()\n",
    "\n",
    "# Input CMEMS User and Password (case sensitive)\n",
    "# and desired directory to write data to. \n",
    "# NOTE THAT YOUR PASSWORD CANNOT END WITH AN AMPERSAND - THIS WILL CAUSE THIS TO FAIL\n",
    "USER = ''\n",
    "PASSWORD = ''\n",
    "out_dir = '/glade/scratch/jsimkins/glorys/'\n",
    "new_name = \"test\"\n",
    "# Set Lat/lon bounds\n",
    "min_lon = str(-100)\n",
    "max_lon = str(40)\n",
    "min_lat = str(-20)\n",
    "max_lat = str(90)\n",
    "\n",
    "\n",
    "def name_from_day(day_string):\n",
    "    return f'GLORYS_REANALYSIS_{day_string}.nc'\n",
    "\n",
    "\n",
    "def get_days_in_year(year):\n",
    "    all_days = pd.date_range(f'{year}-01-01', f'{year}-12-31')\n",
    "    day_strings = [d.strftime('%Y-%m-%d') for d in all_days]\n",
    "    return day_strings\n",
    "\n",
    "\n",
    "def download_day(day_string):\n",
    "    t1 = f'{day_string} 00:00:00'\n",
    "    t2 = f'{day_string} 11:59:59'\n",
    "    new_name = name_from_day(day_string)\n",
    "    command = f'python -m motuclient --motu http://my.cmems-du.eu/motu-web/Motu --service-id GLOBAL_MULTIYEAR_PHY_001_030-TDS --product-id cmems_mod_glo_phy_my_0.083_P1D-m --longitude-min {min_lon} --longitude-max {max_lon} --latitude-min {min_lat} --latitude-max {max_lat} --date-min {t1} --date-max {t2} --depth-min 0.493 --depth-max 5727.918 --variable so --variable thetao --variable uo --variable siconc --variable vo --variable zos --out-dir {out_dir} --out-name {new_name} --user {USER} --pwd {PASSWORD}'\n",
    "    os.system(command)\n",
    "\n",
    "\n",
    "def download_year(year):\n",
    "    for day in get_days_in_year(year):\n",
    "        ntries = 0\n",
    "        while not path.isfile(path.join(out_dir, name_from_day(day))):\n",
    "            if ntries > 3:\n",
    "                print(f'Failed to download {day}')\n",
    "                break\n",
    "            download_day(day)\n",
    "            ntries += 1\n",
    "            \n",
    "\n",
    "if __name__ == '__main__':\n",
    "    download_year(2010)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
