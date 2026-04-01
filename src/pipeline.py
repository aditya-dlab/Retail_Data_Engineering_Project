from ingestion import load_data
from transform import transform_data
from load import save_data
from utils.logger import get_logger

logger = get_logger()

def run_pipeline():
    logger.info("Pipeline started")

    try:
        data = load_data()
        logger.info("Data loaded")

        df = transform_data(data)
        logger.info("Data transformed")

        save_data(df)
        logger.info("Data saved")

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        print("Error occurred. Check logs.")

if __name__ == "__main__":
    run_pipeline()