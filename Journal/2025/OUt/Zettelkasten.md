Como tomar notas inteligentes

ef load_menus_before_startup():
    """Carrega os menus ANTES da aplicação abrir de forma segura"""
    try:
        print("📋 Carregando menus antes da inicialização...")
        
        # Verifica se existe o arquivo Excel
        excel_path = os.path.join(os.path.dirname(__file__), '..', 'dados', 'menus_config.xlsx')
        if not os.path.exists(excel_path):
            print("⚠️ Arquivo Excel não encontrado, usando estrutura padrão")
            return False
            
        # Verifica se a verificação automática está disponível
        if not AUTO_UPDATE_AVAILABLE:
            print("⚠️ Verificação automática não disponível, usando estrutura padrão")
            return False
            
        try:
            # Carrega os menus de forma segura
            updater = MenuAutoUpdater("config.py", excel_path)
            new_structure = updater.read_excel_menus()
            
            if new_structure and isinstance(new_structure, dict):
                print("✅ Menus carregados do Excel antes da inicialização")
                # Não modifica variáveis globais aqui para evitar problemas
                return True
            else:
                print("⚠️ Estrutura de menus inválida, usando estrutura padrão")
                return False
                
        except Exception as e:
            print(f"⚠️ Erro ao ler menus do Excel: {e}, usando estrutura padrão")
            return False


      capa_path = self._get_capa_template_path()
        self.docx_processor = DOCXProcessor(capa_path)
        
        # Inicializa a lista para rastrear informações de arquivo por página
        self.page_file_info = []
        
    def _get_capa_template_path(self) -> str:
        """
        Retorna o caminho correto para o arquivo de template da capa
        
        Returns:
            Caminho completo para capa-base.docx
        """
        # Tenta diferentes caminhos possíveis
        possible_paths = [
            # Caminho relativo à pasta dados/ (quando executado da raiz)
            os.path.join("dados", "capa-base.docx"),
            # Caminho relativo ao diretório atual do script
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "dados", "capa-base.docx"),
            # Caminho absoluto baseado na raiz do projeto
            os.path.join(os.getcwd(), "dados", "capa-base.docx")
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                print(f"✅ Template da capa encontrado em: {path}")
                return path
        
        # Se nenhum caminho funcionar, retorna o padrão
        default_path = os.path.join("dados", "capa-base.docx")
        print(f"⚠️ Usando caminho padrão para template da capa: {default_path}")
        return default_path