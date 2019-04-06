def csv_to_mongodb(directory):
    client = pymongo.MongoClient('localhost', 27017)
    db = client.sf_crimes_db
    db_collname = db.sf_crimes
    cdir = os.path.dirname(os.path.realpath('__file__'))
    file_res = os.path.join(cdir, directory)

    df = pd.read_csv(file_res)
    data_json = json.loads(df.to_json(orient='records'))
    db_collname.remove()
    db_collname.insert_many(data_json)

if __name__ == "__main__":
  directory = r'C:\Users\RandallLueck\Dropbox\Syracuse\iSchool\IST652-PythonScript\Project\sf-police-calls-for-service-and-incidents\sf_crime_data.csv' #csv file path
  csv_to_mongodb(directory)
