from fastapi import Request

class Permission:

    @staticmethod
    def checkUserIdParam(
        user_id: int|None,
        request: Request
    ) -> int|None:
        """
        Check param user_id of an endpoint.
        """
        
        # get user log.
        user_log = request.session.get('user', None)
        if user_log == None:
            raise Exception('user not log')
        
        # no param user id, take if of client log.
        if user_id == None:
            return user_log['id']
        
        # if param user send, verify if log as admin.
        if user_log['role_name'].lower() != 'admin':
            raise Exception('user not admin')
        
        # trust user_id send in parameter (only if user log as admin).
        return user_id
        