{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9dc6ab10",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from googletrans import Translator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e88faf15",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-30 19:32:45.857 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run c:\\Users\\karko\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-04-30 19:32:45.872 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from googletrans import Translator\n",
    "\n",
    "# Load crop disease dataset\n",
    "df = pd.read_csv(\"C:/Users/karko/OneDrive/Desktop/Book1.csv\")\n",
    "\n",
    "translator = Translator()\n",
    "\n",
    "# Supported languages\n",
    "language_codes = {\n",
    "    \"english\": \"en\", \"twi\": \"tw\", \"ga\": \"gaa\", \"ewe\": \"ee\", \"hausa\": \"ha\"\n",
    "}\n",
    "\n",
    "def get_crop_disease_info(query):\n",
    "    row = df[df.apply(lambda x: x[\"Crop\"].lower() in query and x[\"Disease\"].lower() in query, axis=1)]\n",
    "    return row.to_dict(orient=\"records\")[0] if not row.empty else {\"response\": \"Crop/disease info not found.\"}\n",
    "# Streamlit UI\n",
    "st.title(\"🌾 Agricultural Chatbot for Farmers in Ghana\")\n",
    "st.write(\"Ask about crop diseases and solutions!\")\n",
    "\n",
    "user_input = st.text_input(\"Enter your crop disease query:\")\n",
    "language = st.selectbox(\"Choose language:\", list(language_codes.keys()))\n",
    "\n",
    "if st.button(\"Get Info\"):\n",
    "    response = get_crop_disease_info(user_input)\n",
    "    \n",
    "    if language != \"english\":\n",
    "        response = {key: translator.translate(value, dest=language_codes[language]).text for key, value in response.items()}\n",
    "    \n",
    "    st.write(response)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
