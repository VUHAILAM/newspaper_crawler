from app.db.models import Sources

class SourceDAO:
    def __init__(self) -> None:
        self.source = Sources()
    
    def get_all_sources(self):
        sources = []
        source_from_db = Sources.objects

        for s in source_from_db:
            sources.append(s.to_json())
        
        return sources