# Right Arm English Auto Runner

This tool automatically summarizes memory data and uploads it to Notion.

## Usage

1. Set your Notion token in `.env_en` file:
   ```
   NOTION_TOKEN_EN=your_secret_token
   ```

2. Update `config/config_en.json` with your Notion database ID.

3. Run the batch file:
   ```
   run_memory_summary_en.bat
   ```

## Files
- `main_en.py`: Main script to summarize and upload.
- `run_memory_summary_en.bat`: Easy runner.
- `modules/`: Supporting functions.
