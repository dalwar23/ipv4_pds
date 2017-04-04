# ipv4_pds
IPv4 prefix delegation structure
# Known Dependencies
> python 3.4

> mysql connector for python 2.14/2.15
# Instructions on how to use bgp data processing tool
### Step 1
Download/Fork/Clone repository. Under mysql-scripts folder **"bgp_data.sql"** file is the database schema.
Use this file to create the database. Once the database is created successfully move onto next step.
### Step 2
Find the file naming **"fileOperations.py"**. Find the lines that defines the location of .gz files and .csv files. Use your prefered location for .gz files and .csv files.

**Original directory stracture:** data/gz-data, data/csv-data, data/tracking-data

Make sure you have placed the tracking files - **csv-tracker.txt** and **gz-tracker.txt** in the correct location with correct permission.
### Step 3
Find the file naming **"dbConnection.py"** and chnage database login credentials.

Load business and meta data into *"t_business_rel_p1"* and *"t_meta_data_s1"* using mysql CLI or 3rd party software like "phpmyadmin". Transfer data from *"v_business_rel"* and *"v_business_rel_2"* to *"t_business_rel_s1"*.
### Step 4
Make sure all the dependecies are met.
### Step 5
Run mainProgram.py with command "python3 mainProgram.py"

# Use the processing tool for IPv6
> Make sure business relation data, meta data, and all delegation data has same number of columns and the delemitar is the same as ipv4. In this case "|". 

> Make sure folder structure remains the same and Database field length is changed accoedingly inside the table structure.
