This project demonstrates an end-to-end Azure Data Engineering pipeline.

Technologies Used:
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- SQL

Pipeline Steps:
1. Azure Data Factory ingests sales data.
2. Data is stored in Azure Data Lake Bronze layer.
3. Databricks processes and cleans the data.
4. Transformed data is stored in Silver/Gold layers.
5. Data is ready for analytics and reporting.
