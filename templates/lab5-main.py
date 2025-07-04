"""Main Application - Strands Agents Workshop"""
import os
import sys
from typing import Dict, Any
from orchestrator_agent import OrchestratorAgent
from model_config import get_configured_model


class StrandsAgentsWorkshopApp:
    """
    Strands Agents Workshop Main Application
    
    Actual implementation of multi-agent system using 
    Agents as Tools pattern.
    """

    def __init__(self, model_id: str = None, user_id: str = "workshop_user"):
        self.model = get_configured_model(model_id)
        self.user_id = user_id
        self.orchestrator_agent = OrchestratorAgent(self.model, user_id)
        
        # 시스템 정보 출력 (원본 방식)
        model_name = type(self.model).__name__
        current_model_id = getattr(self.model, 'model_id', 'unknown')

        print("=" * 60)
        print("🤖 Agents as Tools multi agent demo")
        print("=" * 60)
        print(f"사용자 ID: {user_id}")
        print()
        print("사용 가능한 agent:")
        print("• Search Agent - 지능적 검색 (Wikipedia + DuckDuckGo)")
        print("• Weather Agent - 날씨 정보 (미국 지역)")
        print("• Conversation Agent - 일반 대화")
        print("• Orchestrator Agent - 오케스트레이터 (Sub Agents 관리)")
        print("=" * 60)

    def process_input(self, user_input: str) -> Dict[str, Any]:
        """사용자 입력을 Orchestrator Agent를 통해 처리"""
        try:
            result = self.orchestrator_agent.process_user_input(user_input)
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"처리 중 오류가 발생했습니다: {str(e)}",
                "user_input": user_input
            }

    def run_single_query(self, query: str) -> Dict[str, Any]:
        """단일 쿼리 실행"""
        return self.process_input(query)

    def format_response(self, response: Dict[str, Any]) -> str:
        """응답 포맷팅 - 시인성 개선"""
        if response.get("success"):
            raw_response = response.get("response", "응답을 생성할 수 없습니다.")
            return raw_response
        else:
            return f"❌ 오류: {response.get('error', '알 수 없는 오류')}"


    def run_single_query(self, query: str) -> Dict[str, Any]:
        """단일 쿼리 실행"""
        return self.process_input(query)

    def run_interactive_mode(self):
        """대화형 모드 실행"""
        print("\n🚀 대화형 모드 시작!")
        print("다양한 요청을 입력해보세요:")
        print("  • 정보 검색: '인공지능에 대해 알려줘'")
        print("  • 날씨 조회: '뉴욕 날씨 어때?'")
        print("  • 복합 요청: '파리에 대해 알려주고 날씨도 알려줘'")
        print("  • 일반 대화: '안녕하세요'")
        print("  • 종료: '/quit'")
        print()

        while True:
            try:
                user_input = input("💬 입력: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['/quit', 'quit', 'exit', '종료']:
                    print("👋 시스템을 종료합니다. 안녕히 가세요!")
                    break
                
                # 요청 처리
                result = self.process_input(user_input)
                response = self.format_response(result)
                
                # 응답 출력 (원본 방식)
                print("\n🎯" + "=" * 58 + "🎯")
                print("🤖 최종 응답")
                print(response)
                print("🎯" + "=" * 58 + "🎯")
                print("\n" + "-" * 50 + "\n")
                
            except KeyboardInterrupt:
                print("\n\n👋 시스템을 종료합니다. 안녕히 가세요!")
                break
            except Exception as e:
                print(f"\n❌ 예상치 못한 오류: {str(e)}")
                print("다시 시도해주세요.\n")


def main():
    """메인 실행 함수""" 
    app = StrandsAgentsWorkshopApp()
    app.run_interactive_mode()


if __name__ == "__main__":
    main()
