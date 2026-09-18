What is CRAG?

CRAG (Corrective Retrieval-Augmented Generation) is an improved version of RAG where the system checks the quality of retrieved documents before generating the final answer.

Normal RAG:

Question → Retrieve documents → LLM → Answer

CRAG:

Question → Retrieve documents → Evaluate retrieval → Correct/Improve retrieval → LLM → Answer

The main purpose is to reduce hallucinations caused by irrelevant or low-quality retrieved documents.

                    USER QUERY
                        │
                        ▼
              ┌──────────────────┐
              │ Query Processing │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Document Retriever│
              │ Vector DB / BM25 │
              └────────┬─────────┘
                       │
                       ▼
              Retrieved Documents
                       │
                       ▼
              ┌──────────────────┐
              │ Retrieval        │
              │ Evaluator        │
              └────────┬─────────┘
                       │
              ┌────────┴────────┐
              │                 │
          GOOD/RELEVANT      BAD/UNCERTAIN
              │                 │
              ▼                 ▼
       Knowledge             Web Search /
       Refinement            Alternative Retrieval
              │                 │
              └────────┬────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Knowledge        │
              │ Refinement       │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │      LLM         │
              │ Answer Generator │
              └────────┬─────────┘
                       │
                       ▼
                  FINAL ANSWER


