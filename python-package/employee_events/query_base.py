# Import any dependencies needed to execute sql queries
from sql_execution import QueryMixin, query

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase:

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name=""

    # Define a `names` method that receives
    # no passed arguments
    # no passed arguments
    def names(self):
        
        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):


        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
       query = f"""
                    SELECT 
                            e.event_date,
                            SUM(e.positive_events) as pos_events_per_day,
                            SUM(e.egative_events) as neg_event_per_day 
                    FROM {self.name}_events e
                    JOIN {self.name} t ON e.{self.name}_id = t.{self.name}_id
                    WHERE t.{self.name}_id = {id}
                    GROUP BY event_date
                    ORDER BY event_date
        """
        df=pandas_query(query)
        return df    
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, id):
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        query = f"""
                    SELECT  
                            n.note_date,
                            n.note
                    FROM {self.name} t
                    JOIN notes n ON t.{self.name}_id = n.{self.name}_id
                    WHERE t.{self.name}_id = {id}
                    ORDER BY note_date DESC
        """
        
        # Execute query and return pandas dataframe
        df=pandas_query(query)
        return df
